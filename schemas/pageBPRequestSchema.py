# -*- coding: utf-8 -*-
"""
File Name: pageBPRequestSchema.py
Description: This module defines the Pydantic schema for the PageBP request.
Author: MathTeixeira
Date: July 19, 2024
Version: 1.0.0
License: MIT License
Contact Information: mathteixeira55
"""

from pydantic import BaseModel, Field, ConfigDict


class PageBPRequestSchema(BaseModel):
  """
  Pydantic schema for the PageBP request.

  This schema defines the structure of the PageBP request sent to the API.

  Attributes:
    businessInfo (str): The businessInfo to be sent.
  """
  businessInfo: str = Field(..., description="The businessInfo to be sent")

  model_config = ConfigDict(
      json_schema_extra={
          "example": {
              "businessInfo":
                  "What is the name of your business? JobSwipe\nWhat product or service will your business offer? An app similar to tinder where candidates will create profiles and companies will create job descriptions. The candidates will swipe to the right the job posting they like, and the companies will swipe to the right the candidates they like. When a candidate swipe a job to the right and the company swipe that candidate to the right it will be a match.\nWhat problem does your product or service solve for your target market? It makes easier and more fun to find good positions and candidates who fits well for that position\nWho is your target market? Please provide details such as demographics, location, and specific needs. People looking for job, and companies looking for employees, specially young people who are used to use smartphone apps. The initial focus will be on Canadian job market.\nWhat is your unique selling proposition (USP) or competitive advantage? The app will use and algorithm to higher the chances of a good match between candidates skills and job positions, lessening HR work and candidates repetitive tasks\nWhat are your short-term and long-term business goals? In a short term, we want to gain as many users as possible, starting with Ontario market. Final goal is to make the app be used worldwide and make a sustainable business that will make profits out of advertising, sponsoring, subscriptions, and so on...\nWhat marketing strategies will you use to promote your product or service? First, approach colleges to get their COOP companies partners and their students to use the app. Later use social media and other kind of internet advertising.\nWhat is your revenue model? How will your business make money? We will make profits out of advertising, sponsoring, subscriptions, and so on...\nWho are your main competitors, and what differentiates you from them? Indeed and LinkedIn, maybe. The idea is to facilitate the application and the matches, which are basically done manually on those platforms.\nWhat are your initial funding requirements and how do you plan to use the funds? Initially, I will need to pay the developers, and the cloud infrastructure, but I am not sure how much that would cost me.\n"
          }
      })
