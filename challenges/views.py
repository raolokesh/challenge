from django.shortcuts import render
from django.http import Http404 , HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse


# from django.template.loader import render_to_string
# Create your views here.

# def index(request):
#     return  HttpResponse("this works")

# def february(request):
#     return HttpResponse("this february month")

# def march(request):
#     return HttpResponse("this is march month")


monthly_challenges = {
    "january": "this is the january month",
    "february": "this is the february month",
    "march": "this is the march month",
    "april": "this is the april month",
    "may": "this is the may month",
    "june": "this is the june month",
    "july": "this is the july month",
    "august": "this is the august month",
    "september": "this is the september",
    "october": "this is the october month",
    "november": "this is the november month",
    "december": None
}

def monthly_challenge_by_number(request , month):
    months = list(monthly_challenges.keys())
    if month<len(months):
        forward_month = months[(month-1)]
    else:
        return HttpResponseNotFound("enter correct months")
    
    redirect_path = reverse("monthly-challenge", args=[forward_month])
    return HttpResponseRedirect(redirect_path)
    
    # return HttpResponse(monthly_challenges[forward_month])
    # return HttpResponseRedirect("/challenges/"+ forward_month)

# def monthly_challenge(request, month):
#     challenge_txt = None
#     if month == "january":
#         challenge_txt = "this is the january month"
#     elif month == "march":
#         challenge_txt = "this is the march month"
#     else :
#         return HttpResponseNotFound('this page is not found')
#     return HttpResponse(challenge_txt)

def monthly_challenge(request, month):
    try:
        challenge_txt = monthly_challenges[month]
        # response_data = render_to_string("challenges/challenge.html")
        return render(request , "challenges/challenge.html" , {
            "text" : challenge_txt, 
            # "title" : month.capitalize(),
             "title" : month,

        })
    except:
        # return HttpResponseNotFound("enter correct month")
        raise Http404()

def index(request):
    # response_data = """<h2>
    # <ul>
    # <li><a href = "/challenges/january">January</li>
    # <li><a href = "/challenges/february">february</li>
    # <li><a href = "/challenges/march"> march</li>
    # <li><a href = "/challenges/april">april </li>
    # <li><a href = "/challenges/may">may </li>
    # <li><a href = "/challenges/june">june </li>
    # <li><a href = "/challenges/july"> july</li>
    # <li><a href = "/challenges/august"> august</li>
    # <li><a href = "/challenges/september"> september</li>
    # <li><a href = "/challenges/october">october </li>
    # <li><a href = "/challenges/november">november </li>
    # <li><a href = "/challenges/december">december </li>
    # </ul>
    # </h2>
    # """

    # list_items = ""
    # month_list = list(monthly_challenges.keys())
    # for month in month_list:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("monthly-challenge",args=[month])
    #     list_items += f"<h2><li><a href = {month_path}> {capitalized_month} </a></li></h2>"
    
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
    month_list = list(monthly_challenges.keys())
    return render(request , "challenges/index.html",{
                      "months" : month_list,
                  })