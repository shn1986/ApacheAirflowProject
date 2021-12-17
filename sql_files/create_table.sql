Drop Table IF EXISTS Store;


CREATE TABLE  Store
(
    StoreID integer,
    StoreName varchar(500),
    isActive bit(1),
    images varchar(500),
	CreateDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Drop Table IF EXISTS Game;

CREATE TABLE Game
(
    GameID integer,
    Title varchar(500),
	CreateDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Drop Table IF EXISTS Deal;
CREATE TABLE Deal
(
    DealID varchar(500),
    StoreID integer,
    GameID integer,
    RetailPrice float,
    Price float,
    IsOnSale bit(1),
    CreateDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT FK_StorDeal FOREIGN KEY (StoreID)
    REFERENCES Store(StoreID),
    CONSTRAINT FK_GameDeal FOREIGN KEY (GameID)
    REFERENCES Game(GameID),
);
