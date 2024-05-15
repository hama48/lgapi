from fastapi import APIRouter, Body

from app.ddd.domain.Calculator import Calculator

router = APIRouter()

@router.get('/hello')
def Hello():
    return {'Hello': 'World!'}

@router.post('/subzero')
def sub(minuend: int = Body(), subtrahend: int = Body()):
    return Calculator.subtract_with_zero_if_negative(minuend,subtrahend)