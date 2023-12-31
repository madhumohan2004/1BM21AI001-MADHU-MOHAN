import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from torch.utils.data import DataLoader, TensorDataset

# Load your dataset (replace 'your_dataset.csv' with your actual dataset file)
def load_dataset(file_path):
    data = pd.read_csv(file_path)
    return data

# Data Preprocessing
def data_preprocessing(data):
    # Encode categorical variables using OneHotEncoder
    categorical_columns = ['Education', 'City', 'Gender', 'EverBenched']
    
    onehot_encoder = OneHotEncoder(sparse=False)
    for column in categorical_columns:
        encoded_columns = onehot_encoder.fit_transform(data[column].values.reshape(-1, 1))
        encoded_df = pd.DataFrame(encoded_columns, columns=[f'{column}_{i}' for i in range(encoded_columns.shape[1])])
        data = pd.concat([data, encoded_df], axis=1)
        data.drop([column], axis=1, inplace=True)

    # Handle missing values (you can choose a suitable strategy)
    data.fillna(0, inplace=True)  # Replace missing values with 0 for demonstration

    return data

# Define features and target
def identify_features_and_targets(data):
    X = data.drop(columns=['LeaveOrNot'])
    y = data['LeaveOrNot']
    return X, y

# Data Scaling (Standardization)
def data_scaling(X_train, X_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled

# Convert data to PyTorch tensors
def load_as_tensors(X_train, y_train, X_test, y_test):
    X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
    y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32)
    X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
    y_test_tensor = torch.tensor(y_test.values, dtype=torch.float32)
    return X_train_tensor, y_train_tensor, X_test_tensor, y_test_tensor

# Define the neural network model
class Salary_Predictor(nn.Module):
    def __init__(self, input_size):
        super(Salary_Predictor, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        x = self.sigmoid(x)
        return x

# Training function
def train_model(model, X_train_tensor, y_train_tensor, num_epochs, optimizer, loss_function):
    model.train()
    
    for epoch in range(num_epochs):
        optimizer.zero_grad()
        outputs = model(X_train_tensor)
        loss = loss_function(outputs, y_train_tensor.view(-1, 1))
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 10 == 0:
            print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item()}')

# Evaluation function
def evaluate_model(model, X_test_tensor, y_test_tensor):
    with torch.no_grad():
        model.eval()
        test_outputs = model(X_test_tensor)
        predicted = (test_outputs >= 0.5).float()
        accuracy = (predicted == y_test_tensor.view(-1, 1)).sum().item() / len(y_test_tensor)
        return accuracy * 100

if __name__ == "__main__":
    # Load and preprocess the dataset
    file_path = 'task_1a_dataset.csv'
    data = load_dataset(file_path)
    preprocessed_data = data_preprocessing(data)
    
    # Identify features and targets
    X, y = identify_features_and_targets(preprocessed_data)
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Data scaling
    X_train_scaled, X_test_scaled = data_scaling(X_train, X_test)
    
    # Convert data to PyTorch tensors
    X_train_tensor, y_train_tensor, X_test_tensor, y_test_tensor = load_as_tensors(X_train_scaled, y_train, X_test_scaled, y_test)
    
    # Initialize the model
    input_size = X_train_tensor.shape[1]
    model = Salary_Predictor(input_size)
    
    # Define loss function and optimizer
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    # Training
    num_epochs = 100
    train_model(model, X_train_tensor, y_train_tensor, num_epochs, optimizer, criterion)
    
    # Evaluation
    accuracy = evaluate_model(model, X_test_tensor, y_test_tensor)
    print(f'Test Accuracy: {accuracy:.2f}%')
    
    # Save the trained model if needed
    torch.save(model.state_dict(), 'task_1a_trained_model.pth')
