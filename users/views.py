from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Proflie


def register(request):
    """Register a new user"""


def user_profile(request, user_id):
    """a page for a user to create their profile"""
