<img src="./img/united_nations_2.png" alt="alt text" title="image Title" style="display:inline" align="left"> <h1 style = "display:inline"> United Nations Data Dashboard </h1>
___
In this project i created a simple dashboard using **streamlit** and **streamlit-folium** to display data extracted from world bank. The objective is to analyze easily some key parameters for a selected country.

You can run the dashboard locally by cloning the github repo, or you can run the dashboard by building the image using the Dockerfile and run it in docker.

<br>

<img src="./img/folder_2.png" alt="alt text" title="folder image" style="display:inline" align="left"> <h2 style = "display:inline"> Data </h2>
___
The data were measured by the world bank, and are stored in the **Data** folder in csv format.
In the dashboard we displayed the most important parameters, but you can find more columns in the csv file.

In the Code folder, you can find the  **"water_sanitation_data.csv"**, which stores the data about water and sanitation for different countries, but i decided not to use it due to high number of missing values.

<img src="./img/desktop_computer.png" alt="alt text" title="PC image" style="display:inline" align="left"> <h2 style = "display:inline"> Run locally </h2>
___

If you want to run the dashboard **locally**, clone the github repo by using this command :

```bash
git clone https://github.com/oulebsir-rafik/UN_dashbord.git
```

move to UN_dashboard folder and install the libraries using **requirements.txt** file:

```bash
cd UN_dashbord
pip3 install -r requirements.txt
```

After that run the main.py python file on server port of your choice : 
```bash
streamlit run main.py --server.port=8501
```

Bravo!, you launched the streamlit web app.


<img src="./img/docker.png" alt="alt text" title="Docker image" style="display:inline" align="left"> <h2 style = "display:inline"> Run using Docker </h2>
___

If you want to run the web app using docker you can just copy the **dockerfile** and build the image using this command : 

```bash
docker build -t un_dashboard .
```

You can if the image is created using this command:

```bash
docker images
```

You can run the docker container using this command:

```bash
docker run -p 8501:8501 streamlit
```
Bravo!, you launched the streamlit web app using **Docker**, using this image you can deploy easily this app. 