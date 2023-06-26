css_template = """
<style>
    .container {
        margin: 20px;
        width: 300px;
        height: 400px;
        border-radius: 10px;
        overflow: hidden;
        position: relative;
        box-sizing: border-box;
    }

    .container.ether {
        color: #000000;
        background-color: #c280e8;
    }

    .container.arcane {
        color: #610059;
        background-color: #00d9ff;
    }

    .container.chaos {
        color: #d80101;
        background-color: #000000;
    }

    .container.nature {
        color: #e5ff7b;
        background-color: #208f52;
    }

    .container.spirit {
        color: #ffffff;
        background-color: #656565;
    }

    .img-container {
        width: 100%;
        height: 65%;
        position: relative;
    }

    .img-container img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .info-container {
        width: 100%;
        height: 35%;
        padding: 10px;
    }

    .info-container .info-row,
    .info-container .stats-row {
        display: flex;
        justify-content: space-between;
    }

    .info-container .info-row .name {
        font-weight: bold;
    }

    .info-container .info-row .hp {
        border-radius: 50%;
        background-color: red;
        padding: 5px;
    }

    .info-container .stats-row {
        margin: 1px 0;
    }

    .info-container .description {
        font-style: italic;
        text-align: center;
        font-size: x-small;
    }
</style>
"""