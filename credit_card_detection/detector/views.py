from django.shortcuts import render
from .ml_model import predict_fraud

def home(request):
    result = None
    score = None

    if request.method == "POST":
        try:
            amount = float(request.POST.get("amount", 0))
            hour = int(request.POST.get("hour", 0))
            tx_type = int(request.POST.get("type", 0))
            merchant = int(request.POST.get("merchant", 0))
            location = int(request.POST.get("location", 0))
            freq = int(request.POST.get("freq", 0))

            result, score = predict_fraud(
                amount, hour, tx_type, merchant, location, freq
            )
        except Exception as e:
            result = "Error processing input"
            score = "N/A"

    return render(request, "home.html", {
        "result": result,
        "score": score
    })