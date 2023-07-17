import requests
import json

def sync_device(device_id, device_type, traits):
    # Определите URL-адрес для синхронизации устройства
    url = "https://actions.googleapis.com/v1/smartHome/enterprises/{project-id}/devices/{device-id}:sync"
    
    # Замените {project-id} и {device-id} на соответствующие значения
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {access-token}"
    }
    
    payload = {
        "requestId": "123",
        "agentUserId": "user-123",
        "devices": [
            {
                "id": device_id,
                "type": device_type,
                "traits": traits
            }
        ]
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        print("Устройство успешно синхронизировано")
    else:
        print("Ошибка при синхронизации устройства")
        print(response.text)
