#set page(columns: 2)

= Introduction


#table(
  columns: (1fr, 1fr, 1fr),
  [*Column*], [*Type*], [*Property*],
  [id], [integer], [primary key],
  [name], [varchar(100)], [not null],
  [description], [text], [null],
  [created_at], [timestamp], [not null]
)