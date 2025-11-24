import torch
import torch.nn as nn
import torch.optim as optim

class MeteoriteNet(nn.Module):
    def __init__(self, input_dim=4, hidden_dim=64, output_dim=6):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden_dim, output_dim)
        )

    def forward(self, x):
        return self.fc(x)


def train_nn(X_train, y_train, num_classes, epochs=40):
    device = "cuda" if torch.cuda.is_available() else "cpu"

    X_train_t = torch.tensor(X_train, dtype=torch.float32).to(device)
    y_train_t = torch.tensor(y_train.values, dtype=torch.long).to(device)

    model = MeteoriteNet(output_dim=num_classes).to(device)
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()

    for epoch in range(epochs):
        optimizer.zero_grad()
        outputs = model(X_train_t)
        loss = criterion(outputs, y_train_t)
        loss.backward()
        optimizer.step()

    torch.save(model.state_dict(), "models/meteorite_land_nn_weights.pth")
    return model
