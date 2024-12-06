from django.shortcuts import render

def index(request):
    
    line_data = [65, 59, 80, 81, 56, 55, 40]
    bar_data = [65, 59, 80, 81, 56, 55, 40]
    scatter_data = [
        {'x': -10, 'y': 0},
        {'x': 0, 'y': 10},
        {'x': 10, 'y': 5},
        {'x': 0.5, 'y': 5.5}
    ]
    pie_data = [300, 50, 100]  

    context = {
        'line_data': line_data,
        'bar_data': bar_data,
        'scatter_data': scatter_data,
        'pie_data': pie_data,
    }
    
    return render(request, 'index.html', context)



