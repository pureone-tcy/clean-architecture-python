# PlantUML
## Sequence Diagram
```
@startuml
participant main #89BDDE
participant RestaurantController #9BD4A3
participant RestaurantUseCase #D2A09F
participant ConsoleRepository #9BD4A3
participant Console #9BD4A3
participant "message(domain)"

main -> RestaurantController : run
RestaurantController -> RestaurantUseCase: run
RestaurantUseCase -> ConsoleRepository: init
ConsoleRepository --> Console: DI
ConsoleRepository <-- Console
RestaurantUseCase -> "message(domain)": create Message
RestaurantUseCase <- "message(domain)"
RestaurantUseCase --> ConsoleRepository: "view(message)"
ConsoleRepository --> Console: "view(message)"
@enduml
```