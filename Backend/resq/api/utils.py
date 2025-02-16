import numpy as np
import tensorflow as tf
from .models import Hospital

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
