from rest_framework import serializers
from prueba_tecnica.models import Loan

class LoanSimpleSerializer(serializers.ModelSerializer):

    class Meta:

        model = Loan
        fields = ['id','book','borrower_name','loan_date','return_date','returned']
        read_only_fields = ['id','loan_date']