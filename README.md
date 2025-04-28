# 404: Job Not Found

**404: Job Not Found** is an AI-powered career assistant developed to streamline and enhance the job application process, especially tailored for international students navigating the complexities of job hunting in the U.S. This tool aims to optimize resume quality, improve ATS compatibility, provide tailored job matches, generate personalized cover letters, and offer career support through an AI chatbot.

## Project Objective

- Develop an AI-powered platform to assist job seekers in improving their job application outcomes.
- Provide personalized feedback on resumes to meet ATS standards.
- Generate tailored job recommendations and custom cover letters.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [System Workflow](#system-workflow)
- [Technical Architecture](#technical-architecture)
- [Key Components](#key-components)
- [Results and Insights](#results-and-insights)
- [Setup and Execution](#setup-and-execution)
- [Technologies Used](#technologies-used)
## Introduction

Job searching, particularly for international students in the U.S., is challenging due to unclear rejections and strict visa timelines. **404: Job Not Found** addresses this by providing clear, actionable insights and tailored recommendations to significantly improve job application outcomes.

## Features

- **Resume Scoring:** ATS compatibility scoring to identify how well the resume matches job descriptions.
- **Resume Feedback:** Detailed suggestions on formatting, grammar, content clarity, and structure.
- **Tailored Job Recommendations:** Automated matching and ranking of top jobs suited to the user's profile.
- **Cover Letter Generation:** Customized cover letters tailored to each job description.
- **Career Chatbot:** AI-driven chatbot available for answering job-related queries and providing career guidance.

## System Workflow

1. User uploads a resume and pastes a job description.
2. The system evaluates resume formatting and compatibility with ATS.
3. An ATS match score is generated, highlighting matched and missing keywords.
4. Personalized feedback for improving resume quality is provided.
5. Top 5 tailored job recommendations with individual cover letters are presented.
6. Users can interact with an AI chatbot for additional support and queries.

## Technical Architecture

- **Data Storage:** Formatted resumes in MongoDB; plain text resumes in ChromaDB for ATS compatibility checks.
- **AI and NLP:** OpenAI and custom NLP techniques for resume evaluation and cover letter generation.
- **Agents:** Multiple specialized agents for formatting checks, resume scoring, job matching, and chatbot interactions.

## Key Components

- **Resume Parser:** Extracts and analyzes content from uploaded resumes.
- **ATS Scorer:** Scores resume compatibility against specific job descriptions.
- **Job Recommender:** Identifies and ranks job postings based on resume analysis.
- **Cover Letter Generator:** Creates personalized cover letters for recommended jobs.
- **Interactive Chatbot:** Provides instant career advice and answers to job-seeking questions.

## Results and Insights

- ATS scoring clearly identified missing keywords essential for passing ATS filters.
- Feedback significantly enhanced resume quality by suggesting actionable improvements.
- Job recommendation system effectively provided users with better-matched job opportunities.
- Automated cover letter generation greatly simplified the application process, enhancing personalization.

## Setup and Execution

### Requirements

- Python 3.x
- MongoDB, ChromaDB
- OpenAI API
- Jupyter Notebook (optional for visualization)

### Installation

```bash
pip install -r requirements.txt
```

### Execution

```bash
git clone <repository-url>
jupyter notebook
```

## Technologies Used

- Python
- MongoDB
- ChromaDB
- OpenAI (for NLP and generative tasks)
- AI-driven chatbot technologies



