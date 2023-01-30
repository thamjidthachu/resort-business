# resort-business
```
The application will have a home page to list out the very recent 3 services.
The service listing page lists out only 5 services on a single page and Have pagination feature to shore more services in the next pages.
Each service offering will have a name, Descriptions & multiple images.
The service listing page shows only the Service name and one image.
Selecting the image or name will take the user to the service detail page where the name, description, and all the images under the service are listed.
A logged-in user will be able to comment on the service and all the previous comments received for the service will be listed out in the comment section on top of the comment listing.
The resort Have an admin interface to create and publish the services and view the comments created under each service.
```
#Installation and Configuration

```
cd ./resortbusiness
pip install -r requirements.txt

python ./mange.py migrate
python ./mange.py createsuperuser
python ./mange.py runserver
```



