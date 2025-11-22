# Pet Adoption System

A comprehensive web application for reporting and finding lost/found pets.

## Features

- Advanced pet search with filters
- Report found and lost pets
- User dashboard to manage reports
- Admin panel for request approval
- Real-time notifications
- Contact system
- Fully responsive design

## Installation

### Prerequisites
- Python 3.8+
- MySQL 8.0+
- pip

### Setup Steps

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd pet_adoption_system
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure MySQL Database**
Create a database in MySQL:
```sql
CREATE DATABASE pet_adoption_db;
```

Update `pet_adoption/settings.py` with your MySQL credentials.

5. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Run the server**
```bash
python manage.py runserver
```

8. **Access the application**
- Main site: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/
- Admin dashboard: http://127.0.0.1:8000/dashboard/

## Usage

### For Users
1. Register an account
2. Report found or lost pets
3. Search for pets using filters
4. Track your reports in My Dashboard
5. Receive notifications on request status

### For Admins
1. Login with admin credentials
2. Access admin dashboard
3. Review pending requests
4. Approve or reject pet reports
5. Manage user contacts

## Technologies Used

- **Backend:** Django 5.2
- **Database:** MySQL
- **Frontend:** HTML, CSS, JavaScript
- **Authentication:** Django Auth System

## Project Structure
pet_adoption_system/
├── pets/                 # Main application
│   ├── models.py        # Database models
│   ├── views.py         # View functions
│   ├── forms.py         # Form definitions
│   ├── urls
│   ├── urls.py          # URL routing
│   └── admin.py         # Admin configuration
├── templates/           # HTML templates
│   ├── base.html
│   └── pets/
├── static/              # Static files
│   ├── css/
│   ├── js/
│   └── images/
├── media/               # User uploads
├── pet_adoption/        # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
````

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.

## Support

For support, email info@petadoption.com or contact us through the website.

## Acknowledgments

- Django Documentation
- Bootstrap Icons (if used)
- Unsplash for images
````

### Step 2: Update requirements.txt

Create/update `requirements.txt`:
````txt
Django==5.2.7
mysqlclient==2.2.0
Pillow==10.1.0
django-ratelimit==4.1.0
````

Generate it automatically:
````bash
pip freeze > requirements.txt
````

### Step 3: Create User Documentation

Create `docs/USER_GUIDE.md`:
````markdown
# User Guide - Pet Adoption System

## Getting Started

### Registration
1. Click **Register** in the navigation bar
2. Fill in your details:
   - Username
   - Email
   - Phone (optional)
   - Password (minimum 8 characters)
3. Click **Register**
4. You'll be automatically logged in

### Login
1. Click **Login** in the navigation bar
2. Enter your username and password
3. Click **Login**

## Reporting Pets

### Report a Found Pet
1. Click **Report Found** in the navigation
2. Fill in the form:
   - Pet Type (Dog, Cat, Bird, etc.)
   - Breed
   - Color
   - Location where found
   - Date found
   - Description
   - Upload a photo
3. Click **Submit Report**
4. Wait for admin approval

### Report a Lost Pet
1. Click **Report Lost** in the navigation
2. Fill in the form:
   - Pet Name
   - Pet Type
   - Breed
   - Color
   - Last seen location
   - Date lost
   - Your contact information
   - Description
   - Upload a photo
3. Click **Submit Report**
4. Wait for admin approval

## Searching for Pets

### Basic Search
1. Go to **Search** page
2. Enter keywords in the search box
3. Click **Search**

### Advanced Search
1. Click **Advanced Filters**
2. Select filters:
   - Pet Type
   - Status (Lost/Found)
   - Breed
   - Color
   - Location
   - Date Range
3. Click **Apply Filters**

### Viewing Pet Details
1. Click on any pet card
2. View full information
3. Click **Contact Reporter** to get contact info
4. Use **Email Reporter** to send an email

## Managing Your Reports

### Access Your Dashboard
1. Click **My Dashboard** in navigation
2. View all your reports
3. See request status (Pending/Approved/Rejected)

### Edit a Report
1. Go to **My Dashboard**
2. Find the pet report
3. Click **Edit** (only for pending reports)
4. Update information
5. Click **Update Report**

### Delete a Report
1. Go to **My Dashboard**
2. Find the pet report
3. Click **Delete** (only for pending reports)
4. Confirm deletion

## Notifications

### View Notifications
1. Click **Notifications** in navigation
2. See all your notifications
3. Unread notifications are highlighted

### Mark as Read
1. Click **Mark as Read** on any notification
2. Or click **Mark All as Read** at the top

## Contact Us

### Send a Message
1. Click **Contact** in footer
2. Fill in the form:
   - Name
   - Email
   - Subject
   - Message
3. Click **Send Message**

## Tips

- Upload clear photos of pets
- Provide detailed descriptions
- Include exact locations
- Update your contact information
- Check notifications regularly
- Respond promptly to inquiries

## Troubleshooting

### Can't login?
- Check your username and password
- Use **Forgot Password** if needed

### Photo won't upload?
- Max file size: 5MB
- Supported formats: JPG, PNG, GIF

### Report not showing up?
- Wait for admin approval
- Check status in **My Dashboard**

### Can't edit/delete report?
- Only pending reports can be edited/deleted
- Approved/rejected reports are final

## Privacy & Safety

- Your personal information is protected
- Email addresses are only shown to authenticated users
- Admin approval required for all reports
- Report suspicious activity to admins

## Need Help?

Contact us:
- Email: info@petadoption.com
- Phone: +1-234-567-8900
- Website: Contact form
````

### Step 4: Create Admin Documentation

Create `docs/ADMIN_GUIDE.md`:
````markdown
# Admin Guide - Pet Adoption System

## Admin Access

### Login as Admin
1. Go to http://127.0.0.1:8000/admin/
2. Enter superuser credentials
3. Access Django admin panel

OR

1. Login with admin account
2. Click **Dashboard** in navigation
3. Access custom admin dashboard

## Managing Requests

### View Pending Requests
1. Go to **Dashboard**
2. Click **Pending** tab
3. Review all pending pet reports

### Approve a Request
1. Find the request
2. Click **Approve**
3. Confirm approval
4. User receives notification

### Reject a Request
1. Find the request
2. Click **Reject**
3. Confirm rejection
4. User receives notification

### Filter Requests
- **Pending**: New submissions awaiting review
- **Approved**: Accepted reports (visible to public)
- **Rejected**: Declined reports

## Managing Users

### View Users
1. Go to Django admin: `/admin/`
2. Click **Users**
3. See all registered users

### Make User Admin
1. Find user in admin panel
2. Check **Staff status**
3. Check **Superuser status** (if needed)
4. Save

### Deactivate User
1. Find user
2. Uncheck **Active**
3. Save

## Managing Content

### Edit Pet Reports
1. Go to Django admin
2. Click **Pets**
3. Select pet
4. Edit information
5. Save

### Delete Pet Reports
1. Find pet in admin
2. Click **Delete**
3. Confirm deletion

### View Contact Messages
1. Go to Django admin
2. Click **Contacts**
3. Review messages
4. Mark as resolved

## Notifications

### Admin Notifications
- New pet reports
- Contact messages
- System alerts

### Sending Notifications
Notifications are automatically sent when:
- User submits a report
- Admin approves/rejects request
- User edits their report

## Statistics & Reports

### Dashboard Statistics
- Total pending requests
- Total approved requests
- Total rejected requests

### User Activity
View in Django admin:
- Total users
- Active users
- Recent registrations

## Best Practices

### Reviewing Reports
**Check for:**
- Clear photos
- Detailed descriptions
- Valid locations
- Appropriate content

**Reject if:**
- Spam or fake reports
- Inappropriate content
- Duplicate submissions
- Incomplete information

### Response Time
- Review requests within 24 hours
- Respond to contact messages promptly
- Address user concerns quickly

## Database Management

### Backup Database
```bash
python manage.py dumpdata > backup.json
```

### Restore Database
```bash
python manage.py loaddata backup.json
```

### Clear Old Data
1. Go to Django admin
2. Use filters to find old records
3. Select and delete

## Troubleshooting

### Too Many Pending Requests
- Set aside time for daily reviews
- Prioritize by date
- Use bulk actions if needed

### Spam Reports
- Reject immediately
- Consider banning user if repeated
- Check for patterns

### Database Issues
- Check migrations: `python manage.py showmigrations`
- Run migrations: `python manage.py migrate`
- Check database connection in settings

## Security

### Regular Tasks
- Review user accounts weekly
- Check for suspicious activity
- Update passwords regularly
- Backup database weekly

### If Compromised
1. Change admin password immediately
2. Review recent changes
3. Check user activity logs
4. Restore from backup if needed

## Maintenance

### Regular Maintenance
- **Daily**: Review pending requests
- **Weekly**: Check notifications, backup database
- **Monthly**: Review statistics, clean old data

### Server Maintenance
```bash
# Collect static files
python manage.py collectstatic

# Clear cache (if using caching)
python manage.py clear_cache
```

## Support Escalation

### Critical Issues
1. Database errors
2. Security breaches
3. System downtime
4. Data loss

### Contact Developer
- Document the issue
- Provide error messages
- Include screenshots
- Note steps to reproduce

## Tips for Efficient Management

1. **Set a schedule** - Review requests at specific times
2. **Use filters** - Sort by date, type, status
3. **Communicate** - Keep users informed
4. **Document** - Track patterns and issues
5. **Stay organized** - Archive old requests

## Admin Commands

### Create Superuser
```bash
python manage.py createsuperuser
```

### Change Password
```bash
python manage.py changepassword <username>
```

### Run Server
```bash
python manage.py runserver
```

### Check for Issues
```bash
python manage.py check
```

## FAQ

**Q: How do I handle duplicate reports?**
A: Reject duplicates and notify the user.

**Q: Can I bulk approve requests?**
A: Currently, no. Use Django admin for bulk actions.

**Q: How to export data?**
A: Use Django admin export or dumpdata command.

**Q: How to add another admin?**
A: Make user staff in Django admin panel.

## Need Help?

- Check Django documentation
- Review application logs
- Contact development team
- Check GitHub issues
````

### Step 5: Create Testing Checklist

Create `docs/TESTING_CHECKLIST.md`:
````markdown
# Testing Checklist - Pet Adoption System

## Pre-Testing Setup

- [ ] Database is set up and migrated
- [ ] Superuser is created
- [ ] Test data is prepared
- [ ] All static files are collected
- [ ] Server is running without errors

## User Registration & Authentication

### Registration
- [ ] Can access registration page
- [ ] Form validation works (empty fields)
- [ ] Email validation works (invalid format)
- [ ] Password validation works (too short)
- [ ] Duplicate email shows error
- [ ] Successful registration redirects to home
- [ ] User is automatically logged in
- [ ] Success message displays

### Login
- [ ] Can access login page
- [ ] Invalid credentials show error
- [ ] Valid credentials log in successfully
- [ ] Redirects to home after login
- [ ] Navigation updates (shows logout)

### Logout
- [ ] Logout link works
- [ ] User is logged out successfully
- [ ] Redirects to home
- [ ] Navigation updates (shows login)

## Report Found Pet

- [ ] Login required (redirects if not logged in)
- [ ] Form displays correctly
- [ ] All fields are present
- [ ] Date field shows date picker
- [ ] Image upload works
- [ ] Image preview shows
- [ ] Remove image button works
- [ ] Form validation works
- [ ] Max date is today (cannot select future)
- [ ] File size validation works (>5MB)
- [ ] Successful submission creates pet
- [ ] Request is created with pending status
- [ ] Admin receives notification
- [ ] Success page displays
- [ ] Redirects work correctly

## Report Lost Pet

- [ ] Login required
- [ ] Form displays with all fields
- [ ] Pet name field is present
- [ ] Owner contact field works
- [ ] Image upload works
- [ ] Form validation works
- [ ] Successful submission works
- [ ] Admin receives notification
- [ ] Success page displays

## User Dashboard

- [ ] Login required
- [ ] Statistics display correctly
- [ ] All pet reports are shown
- [ ] Request status is visible
- [ ] Pending reports show edit/delete buttons
- [ ] Approved reports hide edit/delete
- [ ] View button works
- [ ] Empty state shows when no reports

### Edit Pet
- [ ] Only pending reports can be edited
- [ ] Form pre-fills with existing data
- [ ] Image shows current image
- [ ] Can update all fields
- [ ] Can change image
- [ ] Update works successfully
- [ ] Redirects to dashboard
- [ ] Success message shows

### Delete Pet
- [ ] Only pending reports can be deleted
- [ ] Confirmation page shows
- [ ] Pet details display
- [ ] Cancel button works
- [ ] Delete button works
- [ ] Pet is removed from database
- [ ] Success message shows

## Search Functionality

### Basic Search
- [ ] Search page loads
- [ ] Search input works
- [ ] Results display correctly
- [ ] No results message shows
- [ ] Results show relevant pets only

### Advanced Filters
- [ ] Filters toggle works
- [ ] All filter fields present
- [ ] Type filter works
- [ ] Status filter works
- [ ] Breed filter works
- [ ] Color filter works
- [ ] Location filter works
- [ ] Date range filter works
- [ ] Apply filters works
- [ ] Clear filters works
- [ ] Results update correctly

### Search Results
- [ ] Pet cards display correctly
- [ ] Images load properly
- [ ] Status badges show
- [ ] Pet information displays
- [ ] Click to view details works
- [ ] Contact button works
- [ ] Pagination works (if >12 results)

## Pet Detail Page

- [ ] Page loads correctly
- [ ] Breadcrumb navigation works
- [ ] Pet image displays
- [ ] Status badge shows
- [ ] All pet information displays
- [ ] Share buttons work (Facebook, Twitter, Copy)
- [ ] Contact reporter button works (if logged in)
- [ ] Contact modal displays
- [ ] Email reporter link works
- [ ] Similar pets section shows
- [ ] Similar pet links work
- [ ] Back to search works

## Admin Dashboard

### Access
- [ ] Non-staff users cannot access
- [ ] Staff users can access
- [ ] Dashboard loads correctly

### Statistics
- [ ] Pending count is correct
- [ ] Approved count is correct
- [ ] Rejected count is correct

### Tabs
- [ ] Pending tab works
- [ ] Approved tab works
- [ ] Rejected tab works
- [ ] Counts display in tabs

### Request Management
- [ ] All requests display correctly
- [ ] Pet images show
- [ ] Pet information shows
- [ ] Reporter information shows
- [ ] Request date shows

### Approve/Reject
- [ ] Approve button shows for pending
- [ ] Reject button shows for pending
- [ ] Modal confirmation shows
- [ ] Approve works correctly
- [ ] Reject works correctly
- [ ] Status updates in database
- [ ] User receives notification
- [ ] Success message shows
- [ ] Page updates correctly

### Pagination
- [ ] Shows if >10 requests
- [ ] Previous button works
- [ ] Next button works
- [ ] Page numbers display

## Notifications

### Notification Badge
- [ ] Badge shows in navigation
- [ ] Unread count displays
- [ ] Badge updates on new notification

### Notifications Page
- [ ] Page loads correctly
- [ ] All notifications display
- [ ] Unread notifications highlighted
- [ ] Read notifications shown differently
- [ ] Icons display correctly
- [ ] Timestamps show ("X ago")
- [ ] Mark as read works
- [ ] Mark all as read works
- [ ] View button works (redirects correctly)
- [ ] Pagination works

### Notification Types
- [ ] New request notification (admin)
- [ ] Status update notification (user)
- [ ] Contact message notification (admin)

## Contact Page

- [ ] Page loads correctly
- [ ] Contact info displays
- [ ] Form displays all fields
- [ ] Form pre-fills if logged in
- [ ] Validation works
- [ ] Submit works
- [ ] Admin receives notification
- [ ] Success page displays
- [ ] Message saved in database

## Responsive Design

### Mobile (320px - 768px)
- [ ] Navigation collapses properly
- [ ] All pages are readable
- [ ] Forms are usable
- [ ] Buttons are tappable
- [ ] Images resize correctly
- [ ] Cards stack vertically
- [ ] Modals display properly

### Tablet (768px - 1024px)
- [ ] Layout adjusts correctly
- [ ] Grid layouts work
- [ ] Navigation works
- [ ] All features accessible

### Desktop (>1024px)
- [ ] Full layout displays
- [ ] All features accessible
- [ ] Optimal user experience

## UI/UX Elements

### Animations
- [ ] Page transitions work
- [ ] Card hover effects work
- [ ] Button hover effects work
- [ ] Loading animations show
- [ ] Smooth scrolling works

### Loading States
- [ ] Form submit shows loading
- [ ] Images show loading state
- [ ] Page loads show spinner
- [ ] Loading doesn't block UI

### Messages
- [ ] Success messages show
- [ ] Error messages show
- [ ] Messages auto-hide after 5s
- [ ] Messages are dismissible

## Security

- [ ] CSRF tokens present in forms
- [ ] Login required for protected routes
- [ ] Staff required for admin routes
- [ ] Users can only edit their own pets
- [ ] Users can only delete their own pets
- [ ] SQL injection protected (Django ORM)
- [ ] XSS protected (template escaping)
- [ ] Passwords are hashed
- [ ] File upload size limited

## Browser Compatibility

- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)
- [ ] Mobile browsers

## Performance

- [ ] Pages load in <3 seconds
- [ ] Images are optimized
- [ ] No console errors
- [ ] Database queries optimized
- [ ] Static files cached

## Edge Cases

- [ ] Empty database shows correctly
- [ ] Very long text handles properly
- [ ] Special characters in input work
- [ ] Large images resize correctly
- [ ] Missing images show placeholder
- [ ] Deleted user's pets remain
- [ ] Concurrent updates handled

## Final Checks

- [ ] All links work
- [ ] No broken images
- [ ] No console errors
- [ ] No 404 errors
- [ ] Forms submit correctly
- [ ] Data persists correctly
- [ ] User flow is smooth
- [ ] Admin flow is smooth

## Post-Testing

- [ ] Document any bugs found
- [ ] Create bug report tickets
- [ ] Fix critical bugs
- [ ] Retest fixed bugs
- [ ] Get final approval

---

**Testing Date:** _______________  
**Tester Name:** _______________  
**Environment:** Development / Staging / Production  
**Status:** Pass / Fail  
**Notes:** _______________
````

### Step 6: Create Deployment Checklist

Create `docs/DEPLOYMENT_CHECKLIST.md`:
````markdown
# Deployment Checklist

## Pre-Deployment

### Code Preparation
- [ ] All features tested
- [ ] No console errors
- [ ] All bugs fixed
- [ ] Code reviewed
- [ ] Comments added
- [ ] Unnecessary code removed

### Settings Update
- [ ] DEBUG = False
- [ ] ALLOWED_HOSTS configured
- [ ] SECRET_KEY changed (production key)
- [ ] Database credentials updated
- [ ] Static files path configured
- [ ] Media files path configured

### Security
- [ ] HTTPS enabled
- [ ] CSRF settings configured
- [ ] Security headers added
- [ ] Admin URL changed (if needed)
- [ ] Rate limiting configured

### Database
- [ ] Production database created
- [ ] Migrations run
- [ ] Superuser created
- [ ] Initial data loaded (if needed)
- [ ] Database backup plan

### Static Files
- [ ] collectstatic run
- [ ] Static files served correctly
- [ ] CSS/JS minified
- [ ] Images optimized

## Deployment Steps

### Server Setup
- [ ] Server provisioned
- [ ] Python installed
- [ ] MySQL installed
- [ ] Virtual environment created
- [ ] Dependencies installed

### Application Setup
- [ ] Code deployed
- [ ] Environment variables set
- [ ] Database connected
- [ ] Migrations run
- [ ] Static files collected

### Web Server
- [ ] Nginx/Apache configured
- [ ] WSGI configured (Gunicorn/uWSGI)
- [ ] SSL certificate installed
- [ ] Domain configured

## Post-Deployment

### Testing
- [ ] Homepage loads
- [ ] All pages accessible
- [ ] Forms work
- [ ] Image uploads work
- [ ] Admin panel works
- [ ] Database queries work
- [ ] Static files load

### Monitoring
- [ ] Error logging configured
- [ ] Performance monitoring setup
- [ ] Uptime monitoring enabled
- [ ] Backup automated

### Documentation
- [ ] Deployment notes documented
- [ ] Server access documented
- [ ] Environment variables documented
- [ ] Backup process documented

## Rollback Plan

- [ ] Previous version backed up
- [ ] Rollback procedure documented
- [ ] Database rollback plan
- [ ] Emergency contacts list

---

**Deployment Date:** _______________  
**Deployed By:** _______________  
**Environment:** _______________  
**Status:** Success / Failed  
````

---
