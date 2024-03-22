from django.shortcuts import render


def index_page(request):
    context = {
        "title": "Comptech - Catalog",
        "goods": [
            {
                "img": "goods/img/rtx4070.png",
                "title": "Відеокарта Gigabyte RTX 4070 Ti SUPER 16Gb WINDFORCE OC ",
                "price": "41 999₴",
            },
            {
                "img": "goods/img/rtx4070.png",
                "title": "Відеокарта Gigabyte RTX 3060 Ti SUPER OC",
                "price": "20 000₴",
            },
            {
                "img": "goods/img/rtx4070.png",
                "title": "Процессор AMD Ryzen 5 5500",
                "price": "4 000₴",
            },
                        {
                "img": "goods/img/rtx4070.png",
                "title": "Відеокарта Gigabyte RTX 4070 Ti SUPER 16Gb WINDFORCE OC",
                "price": "41 999₴",
            },
            {
                "img": "goods/img/rtx4070.png",
                "title": "МАТЕРИНСЬКА ПЛАТА GIGABYTE B450M DS3H WIFI GSRUHNAIOJNVIOSDHFIS JogihIJNGODC fghni",
                "price": "20 000₴",
            },
            {
                "img": "goods/img/rtx4070.png",
                "title": "Процессор AMD Ryzen 5 5500",
                "price": "4 000₴",
            },
        ],
    }
    return render(request, "goods/index.html", context)
