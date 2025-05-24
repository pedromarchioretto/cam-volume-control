import cv2
import mediapipe as mp
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import bleak
import asyncio
import time

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

BLE_LED_CHARACTERISTIC = '0000ffd9-0000-1000-8000-00805f9b34fb'
device = '60:06:2D:00:07:1C'
# Iniciar a captura de vídeo
#async def alterarcor():
  #  async with bleak.BleakClient(device, timeout=10) as client:
    #    await client.write_gatt_char(BLE_LED_CHARACTERISTIC, bytes([0x56, 255, 0, int(vermelho), 0x00, 0xF0, 0xAA]))

cap = cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignorando frame vazio.")
            continue

        # Converter a cor da imagem de BGR para RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Processar a imagem e desenhar as landmarks
        results = hands.process(image)
        
        # Converter a cor da imagem de volta para BGR para renderização
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Obter as coordenadas das landmarks para a ponta do polegar e do indicador
                thumb_tip = np.array([hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x, hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y])
                index_finger_tip = np.array([hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x, hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y])

                # Calcular a distância euclidiana entre as landmarks
                distance = np.linalg.norm(thumb_tip - index_finger_tip)

                # Se a distância for menor que um certo limite, considerar que os dedos estão se tocando
                if distance < 0.10:
                    #vermelho = np.interp(thumb_tip[0], [0.15, 0.95], [0, 255])


                    vol = np.interp(thumb_tip[0], [0.15, 0.95], [maxVol, minVol])
                    print(thumb_tip[0], vol)
                    volume.SetMasterVolumeLevel(vol, None)

                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Exibir a imagem
        cv2.imshow('MediaPipe Hands', image)

        if cv2.waitKey(5) & 0xFF == 27:
            break
    cap.release()
            
if __name__ == '__main__':
    asyncio.run(alterarcor())
