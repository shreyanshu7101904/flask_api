import jwt as webtoken


def jwtTokenCreater(key, value):
    key = key + "saltvalue"
    encoded_val = webtoken.encode(value, key, algorithm='HS256')
    return encoded_val.decode("utf-8")



def jwtTokenVerify(key, value):
    key = key + "saltvalue"
    try:
        decoded_val = webtoken.decode(value, key, algorithm='HS256')
        return True, decoded_val
    except Exception as e:
        return False, "Token Validation Error"

if __name__== '__main__':
    print(jwtTokenCreater("shreyanshu",{"shreyanshu":"abc"}))
    print(jwtTokenVerify("abc","eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYWJjIiwiYXV0aF92YWx1ZSI6InNocmV5YW5zaHUifQ.h_0tyZggPwDLRlATcM0--SqOEsR1ccIlxld172QqSDk"))