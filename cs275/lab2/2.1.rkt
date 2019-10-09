#lang racket
(define merge
  (lambda lat1 lat2
    (cond
      [(null? lat1) cons(lat2)]
      [(null? lat2) cons(lat1)]
      [(< 
      