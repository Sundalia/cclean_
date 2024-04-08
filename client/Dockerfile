# develop stage
FROM node:18.17-alpine as develop-stage
WORKDIR /client
COPY package*.json ./

RUN npm i -g @quasar/cli
COPY . .

# build stage
FROM develop-stage as build-stage
RUN npm install
RUN quasar build

# production stage
FROM nginx:alpine as production-stage
COPY --from=build-stage /client/dist/spa /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]