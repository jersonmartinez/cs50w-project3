from django.forms import ModelForm, ValidationError
from .models import OrderItem

class OrderItemForm(ModelForm):

    class Meta:
        model = OrderItem
        fields = ['menuitem','toppings', 'quantity', 'order', 'extras']

    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)
        self.fields['toppings'].required = False
        self.fields['extras'].required = False


    def clean_toppings(self):
        toppings = self.cleaned_data['toppings']
        num_toppings = self.cleaned_data['menuitem'].num_toppings
        if len(toppings) != num_toppings:
            if num_toppings == 0:
                raise ValidationError(f"You can not select any toppings for this product")
            else:
                raise ValidationError(f"Please select {num_toppings} toppings for this product")
        return(toppings)

    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        return(cleaned_data)
