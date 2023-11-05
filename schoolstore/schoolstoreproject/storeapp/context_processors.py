from department.models import Department,Course
def menu_links(request):
    links=Department.objects.all()
    d = request.GET.get('deptname')
    courses = Course.objects.filter(deptname=d)
    return dict(links=links,courses=courses)

