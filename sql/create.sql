CREATE TABLE IF NOT EXISTS CD (
    ID SERIAL PRIMARY KEY,
    Titre varchar(50) NOT NULL,
    Auteur varchar(50) NOT NULL,
    Genre varchar(50) NOT NULL,
    Prix decimal(5,2) NOT NULL
);

INSERT INTO CD (Titre, Auteur, Genre, Prix) VALUES
('The Dark Side of the Moon', 'Pink Floyd', 'Rock', 19.99),
('The Wall', 'Pink Floyd', 'Rock', 24.99),
('The Division Bell', 'Pink Floyd', 'Rock', 19.99),
('The Final Cut', 'Pink Floyd', 'Rock', 19.99),
('The Endless River', 'Pink Floyd', 'Rock', 19.99),
('The Piper at the Gates of Dawn', 'Pink Floyd', 'Rock', 19.99),
('A Saucerful of Secrets', 'Pink Floyd', 'Rock', 19.99),
('Ummagumma', 'Pink Floyd', 'Rock', 19.99),
('Atom Heart Mother', 'Pink Floyd', 'Rock', 19.99),
('Meddle', 'Pink Floyd', 'Rock', 19.99);