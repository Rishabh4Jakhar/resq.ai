import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from .models import Hospital, Resource, Supplier, CrisisEvent, Alert

def predict_bed_shortage():
    hospitals = Hospital.objects.all().values('available_beds', 'oxygen_supply')
    
    # Convert to NumPy array
    data = np.array([[h['available_beds'], h['oxygen_supply']] for h in hospitals])
    
    # Simple Neural Network for prediction
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(8, activation='relu', input_shape=(2,)),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(optimizer='adam', loss='mse')
    
    # Fake training for demonstration
    model.fit(data, np.random.rand(len(data), 1), epochs=10, verbose=0)
    
    # Predict shortages
    predictions = model.predict(data)
    
    return predictions.tolist()

def predict_shortages():
    resources = list(Resource.objects.values('name', 'quantity', 'location'))
    
    if not resources:
        return {"message": "No resource data available"}

    # Prepare data
    data = np.array([[r['quantity']] for r in resources])
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(data)

    # Simple AI model
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(8, activation='relu', input_shape=(1,)),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='mse')

    # Fake training (for demo purposes)
    model.fit(data_scaled, np.random.rand(len(data_scaled), 1), epochs=10, verbose=0)

    # Predict shortages (low stock)
    predictions = model.predict(data_scaled)
    shortages = [resources[i]['name'] for i in range(len(resources)) if predictions[i] < 0.3]

    return {"shortages": shortages}

def suggest_alternative_suppliers(resource_name):
    suppliers = Supplier.objects.filter(resource_type=resource_name).order_by('-reliability_score', 'cost_efficiency')
    return [{"name": s.name, "score": s.reliability_score, "cost": s.cost_efficiency} for s in suppliers[:3]]

def detect_critical_events():
    # Get latest crisis events
    events = list(CrisisEvent.objects.values('crisis_type', 'severity', 'location'))
    
    if not events:
        return {"message": "No crisis data available"}

    # Convert severity levels to an array
    data = np.array([[e['severity']] for e in events])

    # Simple AI model for crisis detection
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(8, activation='relu', input_shape=(1,)),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='mse')

    model.fit(data, np.random.rand(len(data), 1), epochs=10, verbose=0)

    predictions = model.predict(data)
    critical_events = [events[i] for i in range(len(events)) if predictions[i] > 0.7]

    # Generate alerts for critical events
    for event in critical_events:
        Alert.objects.create(
            crisis_event=CrisisEvent.objects.get(location=event['location']),
            message=f"Critical {event['crisis_type']} detected at {event['location']}!"
        )

    return {"critical_events": critical_events}