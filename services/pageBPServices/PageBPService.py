# -*- coding: utf-8 -*-
"""
File Name: PageBusinessPlan.py
Description: 
Author: mathteixeira55
Date: June 1, 2024
Version: 1.0.0
License: MIT
Copyright: (c) 2024 mathteixeira55
Contact Information:
"""

### Importing the required libraries ###
# BedrockLLM returns a string only, use ChatBedrock to get metadata and text
from langchain_aws import ChatBedrock
from langchain_core.prompts import ChatPromptTemplate

import boto3
from core.config import pageBP, aws

###### end of imports


class PageBPService:
  """Class to provide business plans based on user input using the Bedrock LLM model.

    Properties:
        is_local (bool): determine if the code is running locally or in the cloud
        modelID (string): model id for the LLM model
        maxTokens (int): maximum number of tokens for the response
        criativity (float): criativity for the response
        awsRegion (string): region for the AWS
        bedrockClient (boto3.client): Bedrock client
        llm (ChatBedrock): LLM model
        """

  ############################## Constructor #################################
  def __init__(
              self,
              AWS_SERVICE_NAME: str = pageBP.AWS_SERVICE_NAME,
              AWS_REGION: str = pageBP.AWS_REGION,
              MODEL: str = pageBP.MODEL,
              MAX_TOKENS: int = pageBP.MAX_TOKENS,
              TEMPERATURE: int = pageBP.TEMPERATURE,
              ):
    """Constructor for the BedrockBusinessPlan class.
        
        Args:
            modelID (string): model id for the LLM model
            maxTokens (int): maximum number of tokens for the response
            criativity (float): criativity for the response
            region (string): region for the AWS
        """
    ############################# Properties ###############################
    # --- Bedrock client ---
    self.client = boto3.client(
        service_name=AWS_SERVICE_NAME,
        region_name=AWS_REGION,
        aws_access_key_id=aws.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=aws.AWS_SECRET_ACCESS_KEY,
    )

    # --- Bedrock model ---
    self.model = ChatBedrock(model_id=MODEL,
                             client=self.client,
                             model_kwargs={
                                 'max_tokens': MAX_TOKENS,
                                 'temperature': TEMPERATURE
                             })
    ######################### end Properties ###############################

  ########################### end Constructor ################################

  ################################ Functions #################################
  # ----------------------------- Main functions -----------------------------
  # Function to create a query to the LLM model
  async def businessPlanQuery(self, businessInfo):
    """Query the LLM model for a business plan.

    Args:
        businessInfo (string): the business information provided by the user.

    Returns:
        string: the business plan in HTML format.
    """
    # Prompt template
    prompt = ChatPromptTemplate.from_messages([(
        "system",
        """<role>You are a backend server</role>
<task>Your task is to create a business plan. To do this task, you should follow the provided instructions.</task>
<instructions>
  1. Read the information about the business provided by the user in the form of a questionnaire.
  2. Analyze the provided information about the business and write a professional business plan with the following components: 
	# Title
	## Executive Summary
	## Business Description
	### Product/Service
	### Problem Solved
	## Market Analysis
	### Target Market
	### Competitive Advantage
	## Business Goals
	### Short-term Goals
	### Long-term Goals
	## Marketing Strategy
	## Revenue Model
	## Competitive Analysis
	## Funding Requirements
  3. For each section, you may add any true and relevant information such as background information, statistics, macro and microeconomics, or other pertinent information for the business case.
  4. Write a minimum of 2 paragraphs per section.
  5. Content in a subsection counts as content for the parent section, so if you write a paragraph for the Product/Service subsection and another for the Problem Solved subsection, the minimum of 2 paragraphs for the Business Description section is already satisfied.
  6. The business plan must have a minimum of 4000 words.
  7. The business plan must have a maximum of 4100 words.
  8. Do not simply repeat the information provided by the user.
  9. Write the business plan using the best practices for creating such documents.
  10. The document should be clear and use formal language.
  11. Skip the preamble and provide only the business plan.
  12. Use appropriate Markdown headers to structure the document.
</instructions>
"""
    ), ("user", "{businessInfo}\n\nAssistant:# Title")])
    # LLMChain: passes the prompt and the LLM model
    chain = prompt | self.model

    # Execute the chain using the invoke method
    async for chunk in chain.astream({'businessInfo': businessInfo}):
      yield chunk.content

