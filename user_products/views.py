import json
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProductUser
from .producer import publish
from rest_framework import status


# class LikeView(APIView):
#     def get(self, request):
#         return Response(json.dumps({"data": "tudo certo"}), status=status.HTTP_200_OK)
#
#     def post(self, request, pk):
#         # req = requests.get('http://django:8001/api/users')
#         # print("Request Made")
#         # json_id = req.json()
#         # print(json_id)
#         # try:
#         #     ProductUser.objects.create(
#         #         user_id=json_id['id'],
#         #         product_id=id,
#         #     )
#         #     publish('product_liked', id)
#         #     data = {"data": "Liked"}
#         #     Response(status=status.HTTP_200_OK)
#         # except Exception as error:
#         #     data = {"data": "Product alrealy liked"}
#         #     Response(status=status.HTTP_400_BAD_REQUEST)
#         Response(status=status.HTTP_200_OK)


class LikeView(APIView):
    def get(self, request):
        return Response(
            {
                'data': "Ok"
            }
        )

    def post(self, request, pk):
        req = requests.get('http://django:8001/api/users')
        print("Request Made")
        json_id = req.json()
        print(json_id)
        try:
            ProductUser.objects.create(
                user_id=json_id['id'],
                product_id=pk,
            )
            publish('product_liked', pk)
            print("Liked")
            return Response(
                {
                    'data': pk
                }
            )
        except Exception as error:
            print("Product alrealy liked")
            return Response(status=status.HTTP_400_BAD_REQUEST)
