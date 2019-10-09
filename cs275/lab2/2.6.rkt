#lang racket
(define phone-book 
         '( (barbara 775-1234) (luke 774-2839) (nick 775-0912) (valerie 775-9043) ))

(define person
  (lambda (phone-number phone-book)
    (cond
      [(null? phone-book) 'disconnected]
      [(eq? phone-number (cadr (car phone-book))) (car (car phone-book))]
      [else (person phone-number (cdr phone-book))])))