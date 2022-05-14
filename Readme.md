# Disecto Assignment

## Approach

I have created this application using the Django_rest_framework, I have used reportlab to generate the pdf for the same.

**Live** - https://disectokartik.herokuapp.com/

**Q2/Q3** - https://docs.google.com/document/d/10RvXr5Lt-HPkb40eT2yyMC482ih5MqRSR4C47xGcZ-s/edit?usp=sharing

## Endpoints

- **POST `/register/`:**

Endpoint that accepts the user in the request body, and return a JSON response of all the details related to that user.

Example curl request:
```bash
curl --location --request POST 'https://disectokartik.herokuapp.com/register/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "user":{
        "username":"KartikKapil",
        "password":"kapil@123",
        "password2":"kapil@123",
        "email":"abc@gmail.com",
        "first_name":"Kartik",
        "last_name":"kapil"
    },
    "address":"343 shalimar park",
    "phone_no":"0123456789"
}
```

- **POST `addItem/`:**

Endpoint that accepts a JSON body containing product data, creates objects for that data and return back the objects.

Example curl request:
```bash
curl --location --request POST 'https://disectokartik.herokuapp.com/addItem/' \
--header 'Content-Type: application/json' \
--data-raw '{
   "name":"Pillow",
   "price":100.0,
   "description":"Soft Pillow"

}
'
```

- **POST `addBill/`:**

Endpoint that accepts a JSON body containing Bill data, creates objects for that data and return back the objects.

Example curl request:
```bash
curl --location --request POST 'https://disectokartik.herokuapp.com/addBill/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username":"KartikKapil",
    "list_of_objects":[{
        "Bat":10
    },{"Pillow":2}]
}
'
```
- **POST `updateItem/`:**

Endpoint that accepts a JSON body containing product data to be update, creates objects for that data and return back the objects.

Example curl request:
```bash
curl --location --request POST 'https://disectokartik.herokuapp.com/addBill/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username":"KartikKapil",
    "list_of_objects":[{
        "Bat":10
    },{"Pillow":2}]
}
'
```

- **GET `getPdf/`:**

Endpoint that accepts parameter and generates Bill at runtime using reportLab library.

Example curl request:
```bash
curl --location --request GET 'http://127.0.0.1:8000/getPdf/?username=KartikKapil'
'
```
