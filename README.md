`apt-get update`

`apt-get upgrade`

`sudo apt install python3-pip`

`pip install --no-cache-dir -r requirements.txt`

`wget -c "https://storage.googleapis.com/kaggle-data-sets/945925/1602520/compressed/yolov3.weights.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240428%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240428T162133Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=1e7b3160f408c4593374c85404252aa9f67a01d9187d593098682b6fe885698ccab27bb33e27d3b5e8df027e0afec8c217a37e67bc0c7ea7c1958a2204bd749e41289599bc2512e8d031b7f9a07a7a62fc604a64d05db360f821d40dda634b0c600f27b73e1917c14a4db3ee5d2f25d43495c06037bfa4d1d46d64150d6e1353c5bd5a368e9bbeb8787cbdfc88cc40662374798066e1d160f72c7c82ffd82ee1bb6d88cd141385a0bacb0ed2198a74a4406c89cf8f2c7baec3a327ea2be44635b243fa4a97b6ec8170029af60c429be388f2c05fd19ce97885763e287a824ea77ec0e1c6e5bb8607a0f4d141adb3093cf613e721242698d61c5e48316b197269"` *Download yolov3.weights file*

`mv 'yolov3.weights.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com@kaggle-161607.iam.gserviceaccount.com%2F20240428%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240428T162133Z&X-Goog-Expires=259200&X-Goog-SignedHead' /appUI/yolov3.weights`  *rename file name to the correct one and move to appUI folder*