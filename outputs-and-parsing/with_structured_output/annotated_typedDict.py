from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model=ChatOpenAI()

#schema:
class Review(TypedDict):
    key_themes:Annotated[list[str],"Write down all the ket themes discussed in the review in a list"]
    summary: Annotated[str,"A brief summary of the review"]
    sentiment: Annotated[Literal["pos","neg"], "Return sentiment of the review either positive, negative or neutral. "]
    pros:Annotated[Optional[list[str]],"Write down all the pros inside the list"]
    cons:Annotated[Optional[list[str]],"Write down all the cons inside the list"]
    name:Annotated[Optional[str], "Write the name of the reviewer"]

structured_model= model.with_structured_output(Review)

result= structured_model.invoke("""
   I recently upgraded to the Samsung Galaxy S2 for Ultra, and I must say it's an absolute powerhouse. The Snapdragon 8 Gen 3 processor makes everything lightning fast, whether I'm gaming, multitasking, or editing photos. The 5000 mAh battery easily lasts a full day, even with the heavy use and the 45W fast charging is a lifesaver. The S Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 2200 mAh camera. The night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for the distant objects, but anything beyond 30x loses quality. However, the weight and the size makes it a bit uncomfortable for one hand use. Also, Samsung's One UI still comes with the bloatware. Why do I need five different Samsung apps for things Google already provides? The 1300 price tag is also a hard pill to swallow. Pros, insanely powerful processor, great for gaming and productivity. Stunning 200 mAh camera with incredible zoom capabilities, long battery life with fast charging. S Pen support is unique and useful. Cons, bulky and heavy, not great for one-handed use. Bloatware still exists in One UI. Expensive compared to competitors. Review by Zedd
""")

print(result['key_themes'])
print(result['summary'])
print(result['name'])