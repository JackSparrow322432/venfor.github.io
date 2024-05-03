import pandas as pd

def export_users_to_excel(request):
    users = User.objects.all()
    user_data = {
        'username': [user.username for user in users]
    }
    df = pd.DataFrame(user_data)
    df.to_excel('users.xlsx', index=False)
    return redirect('file:///C:/Users/User/AppData/Local/Temp/Rar$EXa14288.41501/rest12/index.html')

