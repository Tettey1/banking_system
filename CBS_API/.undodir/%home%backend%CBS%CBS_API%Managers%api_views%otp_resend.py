Vim�UnDo� �S����l�S2��K�Y�0\��H���q,��   A                                   e��    _�                             ����                                                                                                                                                                                                                                                                                                                                                             e��    �                  �               �               5��                                                �                   5                      .      5�_�                       
    ����                                                                                                                                                                                                                                                                                                                                                             e��    �         7      Pfrom staff.utils import generate_and_send_verification_code, get_user_from_token5��                        �                     �                        �                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e��    �                 from django.conf import settings5��                          +      !               5�_�                    
        ����                                                                                                                                                                                                                                                                                                                                                             e��    �   	      6       5��    	                      _                     5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             e��    �   7            �   6   8           �   5   7              )�   4   6          I        {"message": f"OTP resent to {email}.", "status": 200}, status=200�   3   5              return JsonResponse(�   2   4           �   1   3          .    generate_and_send_verification_code(email)�   0   2          K    # Send the new OTP to the user's email using your email sending service�   /   1           �   .   0          F    cache.set(f"email_sent_time-{email}", timezone.now(), timeout=300)�   -   /          2    # Generate a new OTP and store it in the cache�   ,   .           �   +   -          T        return JsonResponse({"message": "Invalid token", "status": 401}, status=401)�   *   ,              except Exception:�   )   +                  email = user.email�   (   *              try:�   '   )           �   &   (          T        return JsonResponse({"message": "Invalid token", "status": 401}, status=401)�   %   '               except ValidationError as e:�   $   &           �   #   %          )        user = get_user_from_token(token)�   "   $              try:�   !   #           �       "          	        )�      !          X            {"message": "Authorization header not provided.", "status": 400}, status=400�                         return JsonResponse(�                    if not token:�                 �                C    token = request.headers.get("Authorization", "").split(" ")[-1]�                    # Get authorization header�                    """�                        None.�                    Raises:�                 �               /        JsonResponse: A JSON response indicating the status of the OTP resend operation. If successful, the response will have a status code of 200 and a message indicating that the OTP has been resent. If there is an error, the response will have a status code of 400 and a corresponding error message.�                    Returns:�                 �                7        request (HttpRequest): The HTTP request object.�                	    Args:�                 �                4    Resends an OTP code to the user's email address.�                    """�                "def otp_code_resend_view(request):�                @require_POST�                @csrf_exempt�   
              �   	              �      
           �      	          2from django.core.exceptions import ValidationError�                5from django.views.decorators.http import require_POST�                Sfrom Managers.utils import generate_and_send_verification_code, get_user_from_token�                4from django.views.decorators.csrf import csrf_exempt�                !from django.utils import timezone�                $from django.http import JsonResponse�                #from django.core.cache import cache�                  5��                        #                   #       �               #       $   $       #       $       �               $       !   I       $       !       �               !       4   k       !       4       �               4       S   �       4       S       �               S       5   �       S       5       �               5       2   *      5       2       �               2           ]      2               �                           ^                      �    	                      _                     �    
                      l                     �                      "   z             "       �                         �                    �               "       4   �      "       4       �                          �                     �               4       	   �      4       	       �                       7   �              7       �               	                 	               �               7                7              �                       /  +              /      �                          [                     �               /         \      /             �                          h                     �                         v                    �                         ~                    �                      C   �             C       �                          �                     �               C          �      C              �                          �                     �                                             �                      @                @       �               X          `      X              �                	          ~      	              �    !                      �                     �    "                      �                     �    #           )          �      )              �    $                   )   �              )       �    %                       �                      �    &           T           �      T               �    '                      �                     �    (                  '                '       �    )                     A                    �    *                  
   [             
       �    +           T       '   f      T       '       �    ,                       �                      �    -           2          �      2              �    .           F          �      F              �    /                      �                     �    0           K          �      K              �    1           .       '   �      .       '       �    2                                           �    3                  
   )             
       �    4           I       '   4      I       '       �    5                      \                     �    6                   2   ]              2       �    7               
       �              M      5��