from django.shortcuts import render,HttpResponse
from collections import Counter

from .forms import StringForm


def can_be_made_from_string(master_str: str, sub_strings: list):
    counter_dict = Counter(master_str)
    substring_exists_dict = {}
    for sub_string in sub_strings:
        sub_string_exists = 'YES'
        for letter in sub_string:
            if not counter_dict.get(letter, 0) > 0:
                sub_string_exists = 'NO'
                break
            else:
                counter_dict[letter]-=1

        substring_exists_dict[sub_string] = sub_string_exists
    return substring_exists_dict

def check_string(request):



	
	if request.method == 'POST':
		
		form = StringForm(request.POST or None,request.FILES)

		
		if form.is_valid():
			master_string=request.POST['master_string']
			string1=request.POST['string1']
			string2=request.POST['string2']
			string3=request.POST['string3']
			string4=request.POST['string4']

			output=can_be_made_from_string(master_string,[string1,string2,string3,string4])
			   
			
			return render(request,'result.html',{'output':output})

	
	else:
		form = StringForm()

	return render(request, 'string.html', {'form': form})
