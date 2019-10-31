@startuml
box "UI Layer" #LightBlue
    participant main #89BDDE
end box

box "Interface Adapters" #LightGreen
    participant RestaurantController #9BD4A3
end box

box "Application Business Rules" #LightPink
    participant RestaurantUseCase #D2A09F
    participant IORepository #D2A09F
end box

box "Interface Adapters" #LightGreen
    participant Console #9BD4A3
end box

box "Enterprise Business Rules" #LightYellow
participant "message(domain)"
end box

main -> RestaurantController : run

activate RestaurantController
RestaurantController -> RestaurantUseCase: init
RestaurantUseCase -> IORepository: init
IORepository -> Console: DI
IORepository <-- Console
RestaurantUseCase <-- IORepository
RestaurantController <-- RestaurantUseCase
RestaurantController -> RestaurantUseCase: run
deactivate RestaurantController

RestaurantUseCase -> "message(domain)": create Message
RestaurantUseCase <- "message(domain)"
RestaurantUseCase --> IORepository: "view(message)"
IORepository --> Console: "view(message)"
Console -> Console: Terminal Output
@enduml