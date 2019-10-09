#lang racket
(define tester? ;tests if it is a sublist
  (lambda (sublist lat)
    (cond
      ((null? sublist) #t)
      ((= (car sublist) (car lat)) (tester? (cdr sublist) (cdr lat)))
      (else #f))))

(define rember-sublist
  (lambda (sublist lat)
    (cond
      [(null? lat) null]
      [(null? sublist) cons lat]
      [(and (pair? lat) (pair? sublist)) (cond ;if both are lists
                             [(= (car sublist) (car lat)) (cond ;if 
                                                            [(tester? sublist lat) (rember-sublist (cdr sublist) (cdr lat))]
                                                            [else (cons(car lat) (rember-sublist sublist (cdr lat)))])]
                             [else (cons(car lat) (rember-sublist sublist (cdr lat)))])])))