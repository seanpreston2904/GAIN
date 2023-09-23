import openai
import os
from dotenv import load_dotenv

if __name__ == "__main__":

    # Load environment variables
    load_dotenv()

    OPENAI_KEY = os.getenv("OPENAI_KEY")
    print(OPENAI_KEY)