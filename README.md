# Simplicitea
The latest revolution in tea-delivery technology is here! Simplicitea combines the selection of over 10 types of tea with a variety of quantity and shipping options to provide YOU with the best tea-drinking experience possible. All while keeping it simple and easy to use. It's simplcitea.

Final project for grade 11 computer science.

## keys.py
The credentials to login to gmail's servers must be defined in a seperate file called keys, which contains the following variables:


```
sender_address = 'example@gmail.com'
sender_pass = 'password or app password if using 2fa'
```

## firebase.json
The code uses a Firebase datastore for recieving and documenting orders. Instructions on setting one up can be found [here](https://firebase.google.com/docs/firestore/quickstart). When you download your private key, rename it to `firebase.json` and place it in the root of the project folder (same directory as main)