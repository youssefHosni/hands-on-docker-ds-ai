from transformers import pipeline

# A small sentiment model from the Hugging Face Hub, downloaded on first use
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
)

reviews = [
    "This movie was a wonderful surprise.",
    "The build failed again and nobody knows why.",
    "Docker made our model deployment painless.",
]
for review, result in zip(reviews, classifier(reviews)):
    print(f"{result['label']:>8} ({result['score']:.3f})  {review}")
