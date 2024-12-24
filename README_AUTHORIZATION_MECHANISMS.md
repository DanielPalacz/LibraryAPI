# Permission Mechanisms in Django and DRF

This document provides a breakdown of various permission mechanisms in Django and Django REST Framework (DRF). It categorizes each mechanism based on whether it applies to Django, Django + DRF, or just DRF.

| **Mechanism**                                | **Django**                        | **Django + DRF**                | **DRF Only**                  |
|----------------------------------------------|-----------------------------------|---------------------------------|-------------------------------|
| **1.1 AllowAny**                             | No                                | No                              | Yes                           |
| **1.2 IsAuthenticated**                      | No                                | No                              | Yes                           |
| **1.3 IsAdminUser**                          | Yes (partially: `is_staff`)       | No                              | Yes                           |
| **1.4 IsAuthenticatedOrReadOnly**            | No                                | No                              | Yes                           |
| **1.5 DjangoModelPermissions**               | Yes                               | Yes                             | No                            |
| **1.6 DjangoObjectPermissions**              | Yes                               | Yes                             | No                            |
| **1.7 Custom classes based on `BasePermission`** | No                                | No                              | Yes                           |
| **1.8 RBAC (Role-Based Access Control)**     | No                                | Yes (typically custom)          | Yes (if custom)               |
| **1.9 DjangoModelPermissionsOrAnonReadOnly** | No                                | No                              | Yes                           |
| **1.10 AllowSpecificHTTPMethods (custom)**   | No                                | No                              | Yes                           |
| **1.11 Complex conditions (e.g., `IsAuthenticatedAndAdmin`)** | No                                | No                              | Yes                           |
| **1.12 CsrfExemptSessionAuthentication**     | Yes (CSRF in Django)              | Yes                             | No                            |
| **1.13 No global permissions**               | Yes                               | Yes                             | No                            |

## Explanation of Categories

- **Django**: These permission mechanisms apply to the Django framework itself, particularly for handling traditional views and models.
- **Django + DRF**: These mechanisms apply to both Django and DRF and often involve Django's ORM or view-related permissions extended by DRF features.
- **DRF Only**: These mechanisms are specific to DRF and are used primarily for API endpoints or working with serialized data.

## Additional Notes

- Mechanisms like `IsAdminUser` and `DjangoModelPermissions` are more tightly coupled with Django's user model and its traditional approach to permissions.
- Many advanced permission mechanisms, such as custom classes based on `BasePermission`, are exclusive to DRF, as they cater to API-specific access control.
- **RBAC** (Role-Based Access Control) typically requires a custom solution and is usually implemented on top of the default Django/DRF permissions model.
- Permission-based strategies like `AllowSpecificHTTPMethods` or `Complex conditions` are often custom implementations to meet specific application needs.
