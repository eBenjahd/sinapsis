from rest_framework.permissions import BasePermission

class IsAuthenticatedUser(BasePermission):

    def has_permission(self, request, view):

        return request.user.is_authenticated
    

class IsStreamer(BasePermission):

    def has_permission(self, request, view):

        return request.user.is_streamer
    

class IsEmailVerified(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.is_email_verified
    

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):

    """
        SIRVE PARA VERIFICAR QUE SOLO EL AUTHOR
        PUEDA MODIFICAR SU PROPIO UPLOAD/ELEMENTO/ETC
    """

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:

            return True

        return obj.author == request.user
    
class CanCreate(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated


class IsOwnerOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        
        return obj.author == request.user
    

class IsChatMember(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
    
        return obj.members.filter(
            id=request.user.id
        ).exists()
    

class IsPremiumUser(BasePermission):

    def has_permission(self, request, view):
        
        return request.user.plan == 'premium' or request.user.plan == 'entreprise'
    
class IsPremiumUserChatGPT(BasePermission):

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        return request.user.plan in [
            "premium",
            "enterprise"
        ]
    

class IsPostOwnerAndVerified(BasePermission):

    def has_permission(self, request, view):

        return request.user.is_authenticated and request.user.is_email_verified
    
    def has_object_permission(self, request, view, obj):
        
        return request.user.id == obj.author.id


class IsModerator(BasePermission):

    def has_permission(self, request, view):

        return request.user.is_moderator
    

class IsCommentOwner(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        
        if request.method in SAFE_METHODS:

            return True
        
        return obj.author == request.user
    

class CanCreateProduct(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_seller
    

class IsOrderOwner(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user
    

class IsProjectMember(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated 

    def has_object_permission(self, request, view, obj):

        return obj.members.filter(
            pk = request.user.id
        ).exists()
    

class IsPlaylistOwner(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated 
    
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        
        return obj.owner == request.user