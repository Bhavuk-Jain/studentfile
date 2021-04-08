#post,get,patch,delete
#localhost:p/api/employeep
from employeeapi.viewsets import EmployeeViewset
from rest_framework import routers
router=routers.DefaultRouter()
router.register('employee',EmployeeViewset)