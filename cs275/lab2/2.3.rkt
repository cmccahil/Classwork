#lang racket
(define helper
  (lambda (sublist lat)
    (cond
      [(null? sublist) #t]
      [(= (car sublist) (car lat)) (helper (cdr sublist) (cdr lat))]
      [else #f])))

(define contains-sublist
  (lambda (sublist lat)
    (cond
      [(null? lat) #f]
      [(= (car sublist) (car lat)) (cond
                                     [(helper sublist lat) #t]
                                     [else (contains-sublist sublist (cdr lat))])]
      [else (contains-sublist sublist (cdr lat))])))