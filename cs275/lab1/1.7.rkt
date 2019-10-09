#lang racket
(define singleElement
  (lambda(a lat)
    (cond
      [(null? lat) #f]
      [(eq? a (car lat)) #t]
      [else (singleElement a (cdr lat))])))

(define allmembers
  (lambda(lat1 lat2)
    (cond
      [(null? lat1) #t]
      [(singleElement (car lat1) lat2) (allmembers (cdr lat1) lat2)]
      [else #f])))