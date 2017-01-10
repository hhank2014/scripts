#add tomcat pid
CATALINA_PID="$CATALINA_BASE/tomcat.pid"
#add java opts
CATALINA_OPTS="-Djava.library.path=/usr/local/tomcat-native/lib"

JAVA_OPTS="-server -Xms512M -Xmx512M -Duser.timezone=UTC -Dspring.profiles.active=test"
