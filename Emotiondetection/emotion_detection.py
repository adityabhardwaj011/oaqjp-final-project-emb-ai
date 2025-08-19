import requests
import json

def emotion_detector(text_to_analyze):
    # api endpoint url i.e. api is Watson NLP service and endpoint /EmotionPredict part of the URL is the specific function we want to use
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Creating myobj which will contain data to be analysed 
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Headers are like special instructions written on the outside of the package. They provide extra information, or metadata, that helps the receiving server understand and process the request correctly.
    # Out of all the tools you have, please use this exact emotion detection model to handle my request
    # headers with the required model ID(key(the information is the id for the ml model i want to use)-value(This is the actual name of the specific AI model on the server that is trained to analyze emotions in English text) pair) for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = response.json()

    # Extracting emotion scores if success
    if response.status_code == 200:
        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotion_scores['anger']
        disgust_score = emotion_scores['disgust']
        fear_score = emotion_scores['fear']
        joy_score = emotion_scores['joy']
        sadness_score = emotion_scores['sadness']
       # Find the dominant emotion
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    elif response.status_code == 400:
         # Handle cases where the input is blank
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    # Format the final output
    formatted_output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    return formatted_output
    return f'{dominant_emotion} is the dominant emotion'

