
## Non-Core 1: Train MNIST MLP End-to-End

Write a complete training pipeline for a 2-layer MLP on MNIST. Single file, no wrappers.

```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        ...
    def forward(self, x):
        ...

def train_epoch(model, loader, criterion, optimizer, device): ...
def evaluate(model, loader, device): ...
def main(): ...

if __name__ == "__main__":
    main()
```

**Requirements:**
1. Dataset: `torchvision.datasets.MNIST`, transforms: `ToTensor()`, `Normalize((0.1307,), (0.3081,))`. DataLoader: batch_size=64, shuffle=True for train.
2. Model: `Linear(784, 128)` → `ReLU` → `Linear(128, 10)`. Flatten 28x28 → 784.
3. Loss: `CrossEntropyLoss`. Optimizer: `Adam(lr=1e-3)`.
4. Train 3 epochs. Print loss every 100 batches: `Epoch X, Batch Y, Loss Z.ZZZ`. Use `.train()` mode.
5. Eval after each epoch on test set. Report: `Test Accuracy: XX.XX%`. Use `.eval()` + `torch.no_grad()`.
6. Save `model.state_dict()` to `checkpoint.pth`.

**Target:** ≥95% test accuracy after 3 epochs. Keep code ≤150 lines.

---

## Non-Core 2: PyTorch Debugging Drill

Find and fix all 5 bugs in this training script. Each bug has a category: shape error, exploding loss, bad normalization, device mismatch, or incorrect mode.

```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

X = torch.randn(1000, 10)
y = torch.randint(0, 3, (1000,))
dataset = TensorDataset(X, y)
loader = DataLoader(dataset, batch_size=32)

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(10, 50)
        self.fc2 = nn.Linear(50, 3)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)  # BUG 1: missing final activation?

model = Net()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=10.0)  # BUG 2

for epoch in range(5):
    model.eval()  # BUG 3
    for X_batch, y_batch in loader:
        # BUG 4: device mismatch
        outputs = model(X_batch)
        loss = criterion(outputs, y_batch)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # BUG 5: shape error in custom metric
        acc = (outputs.argmax(dim=1) == y_batch).float().mean()
        print(f"Loss: {loss.item():.4f}, Acc: {acc.item():.4f}")
```

**Task:** For each bug: (1) name the category, (2) provide the one-line fix, (3) explain why it causes the stated symptom. Write your answers in this format:
```
BUG 1: Category = ...
Fix: ...
Why: ...
```

---

## Wildcard: System Design — Document Processing API

*(Talk-through exercise, no coding. ~1hr.)*

You're building an API for a company that needs to ingest thousands of documents (PDFs, CSVs, Word docs) per day, extract structured data, and make it searchable.

**Talk through:**
- How do you handle different file formats? Plugin architecture vs monolith?
- Sync vs async processing? User uploads → gets result later, or blocks?
- Storage: raw files vs extracted text vs structured output. Where does each live?
- Search: full-text vs embeddings vs both? How do you index?
- What breaks at 10x scale? At 100x?
- How would you add a new document type in 6 months without rewriting?


UNDERSTAND: 
- how would i do rag on my thesis




## Non-Core 1: FastAPI Async Endpoint + Pydantic Schemas

Build a single-file async FastAPI service with Pydantic request/response models.

```python
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from datetime import datetime, timezone
import asyncio

app = FastAPI(title="Hello Async")

class HelloQuery(BaseModel):
    name: str = Field("stranger", description="Name to greet")
    delay_ms: int = Field(0, ge=0, description="Artificial I/O delay in ms")

class HelloResponse(BaseModel):
    message: str
    timestamp: str

@app.get("/hello", response_model=HelloResponse)
async def hello(
    name: str = Query("stranger"),
    delay_ms: int = Query(0, ge=0)
) -> HelloResponse:
    if delay_ms > 0:
        await asyncio.sleep(delay_ms / 1000)
    now = datetime.now(timezone.utc).isoformat()
    return HelloResponse(message=f"Hello, {name}!", timestamp=now)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False)
```

**Requirements:**
1. `GET /hello?name={name}&delay={delay_ms}` — name defaults to "stranger", delay defaults to 0.
2. Response: `{"message": "Hello, <name>!", "timestamp": "2024-11-05T14:23:45.123456+00:00"}`
3. Timestamp must be ISO-8601 UTC.
4. All I/O must be async. Delay simulated with `asyncio.sleep`.
5. Validation errors return 422 automatically.
6. Runnable with `python app.py`.

**Keep it ≤ 60 lines.** The point is to have the FastAPI + Pydantic + async pattern in muscle memory.
