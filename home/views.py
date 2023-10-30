from django.shortcuts import render
from googletrans import Translator, LANGUAGES
from django.http import HttpResponse

def home(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_lan')
        print(input_text)
        if input_text:
            translator = Translator()
            detected_language = translator.detect(input_text).lang
            print(f"Detected Language: {LANGUAGES[detected_language]}")

            target_language = "hi"
            translated_text = translator.translate(input_text, dest=target_language)
            print(f"Translation to {LANGUAGES[target_language]}: {translated_text.text}")

            return render(request, 'index.html', {'input_text':input_text , 'translated_text': translated_text.text})

    return render(request, 'index.html')
