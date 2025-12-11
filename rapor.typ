#set page(columns: 2)

= Giriş

#table(
  columns: (1fr, 1fr, 1fr),
  [*Kolon*], [*Tip*], [*Özellik*],
  [id], [integer], [primary key],
  [ad], [varchar(100)], [not null],
  [aciklama], [text], [null],
  [olusturma], [timestamp], [not null]
)