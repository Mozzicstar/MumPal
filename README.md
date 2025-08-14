# HelpMumPal - Maternal Health Companion

## Overview

HelpMumPal is a comprehensive maternal health companion application built with Streamlit, designed to support pregnant women and new mothers across Africa. The application provides AI-powered health guidance, health tracking, emergency support, and educational resources through an intuitive web interface. It features a modular page-based architecture with session state management for user data persistence and focuses on accessibility and community-centered care for African maternal health contexts.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: Streamlit web application framework
- **Architecture Pattern**: Multi-page application with modular page structure
- **Navigation**: Sidebar-based navigation with emoji-enhanced menu items
- **State Management**: Streamlit session state for user data persistence
- **Layout**: Wide layout with responsive column-based designs
- **UI Components**: Tab-based interfaces, forms, buttons, and interactive widgets

### Application Structure
- **Main Application**: `app.py` serves as the entry point and router
- **Page Modules**: Organized in `pages/` directory with individual modules for each feature
- **Session Management**: User data stored in `st.session_state` including pregnancy week, baby age, reminders, health logs, and emergency contacts
- **Page Routing**: Radio button-based navigation system routing to appropriate page modules

### Core Features Architecture
- **AI Assistant**: Keyword-based response system with predefined health guidance responses
- **Health Tracking**: Form-based data collection with vital signs, mood tracking, and symptom logging
- **Baby/Pregnancy Tracker**: Stage-specific tracking with milestone and development information
- **Nutrition Guide**: Stage-based nutritional guidance (pregnancy, breastfeeding, baby nutrition)
- **Reminder System**: Event scheduling with priority levels and frequency options
- **Emergency Support**: Quick access emergency contacts and location-based hospital finder
- **Mental Health**: Self-care techniques, mood tracking, and postpartum depression resources
- **Resource Library**: Curated health resources from international and local organizations

### Data Management
- **Storage**: In-memory session state storage (no persistent database)
- **User Data Structure**: Dictionary-based user profile with health metrics, reminders, and preferences
- **Data Types**: Health logs, reminder objects, user preferences, and tracking metrics

### Design Patterns
- **Modular Architecture**: Each feature implemented as separate page module
- **Session State Pattern**: Centralized user data management through Streamlit session state
- **Form-Based Interaction**: Structured data input through Streamlit forms
- **Tab-Based Organization**: Complex features organized into tabbed interfaces
- **Responsive Design**: Column-based layouts adapting to different screen sizes

## External Dependencies

### Core Framework
- **Streamlit**: Primary web application framework for UI components, routing, and state management

### Python Standard Libraries
- **datetime**: Date and time handling for reminders, health logs, and tracking
- **random**: Used for mental health affirmations and randomized content

### Planned Integrations
- **AI/ML Services**: Framework prepared for integration with external AI services for health guidance
- **Location Services**: Structure in place for hospital finder and emergency location services
- **Notification Systems**: Reminder system designed for future SMS/email notification integration
- **External Health APIs**: Architecture supports integration with health data providers and medical databases

### Resource Dependencies
- **Health Content**: Relies on WHO, CDC, UNICEF, and other health organization guidelines
- **Emergency Services**: References to local emergency numbers (112, 999, etc.) and healthcare facilities
- **Educational Materials**: Curated content from reputable maternal health organizations